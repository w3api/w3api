---
title: TimeZoneNameProvider.getDisplayName()
permalink: /Java/TimeZoneNameProvider/getDisplayName/
date: 2021-01-11
key: Java.T.TimeZoneNameProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimeZoneNameProvider.metodos valor="getDisplayName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String getDisplayName(String ID, boolean daylight, int style, Locale locale)
~~~

## Parámetros
* **boolean daylight**,  {% include w3api/param_description.html metodo=_dato parametro="boolean daylight" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String ID**,  {% include w3api/param_description.html metodo=_dato parametro="String ID" %}
* **int style**,  {% include w3api/param_description.html metodo=_dato parametro="int style" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TimeZoneNameProvider](/Java/TimeZoneNameProvider/)

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
