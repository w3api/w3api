---
title: SpinnerDateModel.SpinnerDateModel()
permalink: /Java/SpinnerDateModel/SpinnerDateModel/
date: 2021-01-11
key: Java.S.SpinnerDateModel
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.SpinnerDateModel.constructores valor="SpinnerDateModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public SpinnerDateModel()
public SpinnerDateModel(Date value, Comparable<Date> start, Comparable<Date> end, int calendarField)
~~~

## Parámetros
* **int calendarField**,  {% include w3api/param_description.html metodo=_dato parametro="int calendarField" %}
* **Comparable&lt;Date&gt; start**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<Date> start" %}
* **Comparable&lt;Date&gt; end**,  {% include w3api/param_description.html metodo=_dato parametro="Comparable<Date> end" %}
* **Date value**,  {% include w3api/param_description.html metodo=_dato parametro="Date value" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[SpinnerDateModel](/Java/SpinnerDateModel/)

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
