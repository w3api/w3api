---
title: AbstractResourceBundleProvider.getBundle()
permalink: Java/AbstractResourceBundleProvider/getBundle
date: 2021-01-04
key: JavaJava.A.AbstractResourceBundleProvider
category: java
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
* **String baseName**,  {% include w3api/param_description.html metodo=_data parametro="String baseName" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [UncheckedIOException](/Java/UncheckedIOException/)

## Clase Padre
[AbstractResourceBundleProvider](/Java/AbstractResourceBundleProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.AbstractResourceBundleProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
