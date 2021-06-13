---
title: ResourceBundle.Control.needsReload()
permalink: /Java/ResourceBundle/Control/needsReload/
date: 2021-01-11
key: Java.R.ResourceBundle.Control
category: Java
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
* **ClassLoader loader**,  {% include w3api/param_description.html metodo=_dato parametro="ClassLoader loader" %}
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **ResourceBundle bundle**,  {% include w3api/param_description.html metodo=_dato parametro="ResourceBundle bundle" %}
* **long loadTime**,  {% include w3api/param_description.html metodo=_dato parametro="long loadTime" %}
* **String format**,  {% include w3api/param_description.html metodo=_dato parametro="String format" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
