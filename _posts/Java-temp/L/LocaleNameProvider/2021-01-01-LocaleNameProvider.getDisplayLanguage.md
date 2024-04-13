---
title: LocaleNameProvider.getDisplayLanguage()
permalink: /Java/LocaleNameProvider/getDisplayLanguage/
date: 2021-01-11
key: Java.L.LocaleNameProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.L.LocaleNameProvider.metodos valor="getDisplayLanguage" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String getDisplayLanguage(String languageCode, Locale locale)
~~~

## Parámetros
* **String languageCode**,  {% include w3api/param_description.html metodo=_dato parametro="String languageCode" %}
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
