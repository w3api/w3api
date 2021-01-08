---
title: TimeZoneNameProvider.getGenericDisplayName()
permalink: Java/TimeZoneNameProvider/getGenericDisplayName
date: 2021-01-04
key: JavaJava.T.TimeZoneNameProvider
category: java
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
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **int style**,  {% include w3api/param_description.html metodo=_data parametro="int style" %}
* **String ID**,  {% include w3api/param_description.html metodo=_data parametro="String ID" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[TimeZoneNameProvider](/Java/TimeZoneNameProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.T.TimeZoneNameProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
