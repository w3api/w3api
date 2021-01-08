---
title: ResourceBundle.Control.needsReload()
permalink: Java/ResourceBundle/Control/needsReload
date: 2021-01-04
key: JavaJava.R.ResourceBundle.Control
category: java
tags: ['java se', 'java.util', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundle.Control.metodos valor="needsReload" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public boolean needsReload(String baseName, Locale locale, String format, ClassLoader loader, ResourceBundle bundle, long loadTime)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_data parametro="String baseName" %}
* **String format**,  {% include w3api/param_description.html metodo=_data parametro="String format" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **long loadTime**,  {% include w3api/param_description.html metodo=_data parametro="long loadTime" %}
* **ResourceBundle bundle**,  {% include w3api/param_description.html metodo=_data parametro="ResourceBundle bundle" %}
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_data parametro="ClassLoader loader" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ResourceBundle.Control](/Java/ResourceBundle/Control/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.ResourceBundle.Control.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
