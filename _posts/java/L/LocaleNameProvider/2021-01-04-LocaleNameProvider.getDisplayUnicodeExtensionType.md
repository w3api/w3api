---
title: LocaleNameProvider.getDisplayUnicodeExtensionType()
permalink: Java/LocaleNameProvider/getDisplayUnicodeExtensionType
date: 2021-01-04
key: JavaJava.L.LocaleNameProvider
category: java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocaleNameProvider.metodos valor="getDisplayUnicodeExtensionType" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getDisplayUnicodeExtensionType(String type, String key, Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **String key**,  {% include w3api/param_description.html metodo=_data parametro="String key" %}
* **String type**,  {% include w3api/param_description.html metodo=_data parametro="String type" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[LocaleNameProvider](/Java/LocaleNameProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.L.LocaleNameProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
