---
title: ResourceBundleProvider.getBundle()
permalink: Java/ResourceBundleProvider/getBundle
date: 2021-01-11
key: Java.R.ResourceBundleProvider
category: java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.ResourceBundleProvider.metodos valor="getBundle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
ResourceBundle getBundle(String baseName, Locale locale)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Clase Padre
[ResourceBundleProvider](/Java/ResourceBundleProvider/)

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
