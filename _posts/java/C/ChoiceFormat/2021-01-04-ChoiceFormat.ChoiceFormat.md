---
title: ChoiceFormat.ChoiceFormat()
permalink: Java/ChoiceFormat/ChoiceFormat
date: 2021-01-04
key: JavaJava.C.ChoiceFormat
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceFormat.constructores valor="ChoiceFormat" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public ChoiceFormat(double[] limits, String[] formats)
public ChoiceFormat(String newPattern)
~~~

## Parámetros
* **double[] limits**,  {% include w3api/param_description.html metodo=_data parametro="double[] limits" %}
* **String[] formats**,  {% include w3api/param_description.html metodo=_data parametro="String[] formats" %}
* **String newPattern**,  {% include w3api/param_description.html metodo=_data parametro="String newPattern" %}

## Excepciones
[NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ChoiceFormat](/Java/ChoiceFormat/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ChoiceFormat.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
