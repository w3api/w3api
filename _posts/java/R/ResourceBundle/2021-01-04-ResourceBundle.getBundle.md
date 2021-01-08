---
title: ResourceBundle.getBundle()
permalink: Java/ResourceBundle/getBundle
date: 2021-01-04
key: JavaJava.R.ResourceBundle
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundle.metodos valor="getBundle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
static ResourceBundle getBundle(String baseName)
public static ResourceBundle getBundle(String baseName, Module module)
static ResourceBundle getBundle(String baseName, Locale locale)
public static ResourceBundle getBundle(String baseName, Locale locale, ClassLoader loader)
public static ResourceBundle getBundle(String baseName, Locale targetLocale, ClassLoader loader, ResourceBundle.Control control)
public static ResourceBundle getBundle(String baseName, Locale targetLocale, Module module)
static ResourceBundle getBundle(String baseName, Locale targetLocale, ResourceBundle.Control control)
static ResourceBundle getBundle(String baseName, ResourceBundle.Control control)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_data parametro="String baseName" %}
* **Module module**,  {% include w3api/param_description.html metodo=_data parametro="Module module" %}
* **Locale targetLocale**,  {% include w3api/param_description.html metodo=_data parametro="Locale targetLocale" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader loader" %}
* **ResourceBundle.Control control**,  {% include w3api/param_description.html metodo=_data parametro="ResourceBundle.Control control" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/), [NullPointerException](/Java/NullPointerException/), [MissingResourceException](/Java/MissingResourceException/)

## Clase Padre
[ResourceBundle](/Java/ResourceBundle/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceBundle.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
