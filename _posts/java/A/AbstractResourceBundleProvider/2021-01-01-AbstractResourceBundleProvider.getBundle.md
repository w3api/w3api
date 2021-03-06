---
title: AbstractResourceBundleProvider.getBundle()
permalink: /Java/AbstractResourceBundleProvider/getBundle/
date: 2021-01-11
key: Java.A.AbstractResourceBundleProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 9']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.AbstractResourceBundleProvider.metodos valor="getBundle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ResourceBundle getBundle(String baseName, Locale locale)
~~~

## Parámetros
* **String baseName**,  {% include w3api/param_description.html metodo=_dato parametro="String baseName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[UncheckedIOException](/Java/UncheckedIOException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[AbstractResourceBundleProvider](/Java/AbstractResourceBundleProvider/)

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
