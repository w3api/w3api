---
title: CalendarNameProvider.getDisplayNames()
permalink: Java/CalendarNameProvider/getDisplayNames
date: 2021-01-04
key: JavaJava.C.CalendarNameProvider
category: java
tags: ['java se', 'java.util.spi', 'java.base', 'metodo java', 'Java 1.8']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.CalendarNameProvider.metodos valor="getDisplayNames" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Map<String,Integer> getDisplayNames(String calendarType, int field, int style, Locale locale)
~~~

## Parámetros
* **Locale locale**,  {% include w3api/param_description.html metodo=_data parametro="Locale locale" %}
* **String calendarType**,  {% include w3api/param_description.html metodo=_data parametro="String calendarType" %}
* **int field**,  {% include w3api/param_description.html metodo=_data parametro="int field" %}
* **int style**,  {% include w3api/param_description.html metodo=_data parametro="int style" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[CalendarNameProvider](/Java/CalendarNameProvider/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.CalendarNameProvider.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
