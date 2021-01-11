---
title: ResourceBundle.Control.newBundle()
permalink: Java/ResourceBundle/Control/newBundle
date: 2021-01-11
key: JavaJava.R.ResourceBundle.Control
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundle.Control.metodos valor="newBundle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ResourceBundle newBundle(String baseName, Locale locale, String format, ClassLoader loader, boolean reload) throws IllegalAccessException, InstantiationException, IOException
~~~

## Parámetros
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **boolean reload**,  {% include w3api/param_description.html metodo=_dato parametro="boolean reload" %}
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}

## Excepciones
[ExceptionInInitializerError](/Java/ExceptionInInitializerError/), [IllegalArgumentException](/Java/IllegalArgumentException/), [IOException](/Java/IOException/), [SecurityException](/Java/SecurityException/), [ClassCastException](/Java/ClassCastException/), [IllegalAccessException](/Java/IllegalAccessException/), [InstantiationException](/Java/InstantiationException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ResourceBundle.Control](/Java/ResourceBundle/Control/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
