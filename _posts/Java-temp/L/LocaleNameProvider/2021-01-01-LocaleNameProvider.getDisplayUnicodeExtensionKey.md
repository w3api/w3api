---
title: LocaleNameProvider.getDisplayUnicodeExtensionKey()
permalink: /Java/LocaleNameProvider/getDisplayUnicodeExtensionKey/
date: 2021-01-11
key: Java.L.LocaleNameProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocaleNameProvider.metodos valor="getDisplayUnicodeExtensionKey" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getDisplayUnicodeExtensionKey(String key, Locale locale)
~~~

## Parámetros
* **String key**,  {% include w3api/param_description.html metodo=_dato parametro="String key" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[LocaleNameProvider](/Java/LocaleNameProvider/)

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
