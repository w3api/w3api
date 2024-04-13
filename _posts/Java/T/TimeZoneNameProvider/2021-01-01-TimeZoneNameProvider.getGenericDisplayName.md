---
title: TimeZoneNameProvider.getGenericDisplayName()
permalink: /Java/TimeZoneNameProvider/getGenericDisplayName/
date: 2021-01-11
key: Java.T.TimeZoneNameProvider
category: Java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TimeZoneNameProvider.metodos valor="getGenericDisplayName" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public String getGenericDisplayName(String ID, int style, Locale locale)
~~~

## Parámetros
* **int style**,  {% include w3api/param_description.html metodo=_dato parametro="int style" %}
* **Locale locale**,  {% include w3api/param_description.html metodo=_dato parametro="Locale locale" %}
* **String ID**,  {% include w3api/param_description.html metodo=_dato parametro="String ID" %}

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
