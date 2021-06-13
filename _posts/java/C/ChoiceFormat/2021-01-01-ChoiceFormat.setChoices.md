---
title: ChoiceFormat.setChoices()
permalink: /Java/ChoiceFormat/setChoices/
date: 2021-01-11
key: Java.C.ChoiceFormat
category: Java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ChoiceFormat.metodos valor="setChoices" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setChoices(double[] limits, String[] formats)
~~~

## Parámetros
* **double[] limits**,  {% include w3api/param_description.html metodo=_dato parametro="double[] limits" %}
* **String[] formats**,  {% include w3api/param_description.html metodo=_dato parametro="String[] formats" %}

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
{%- for _ldc in _dato.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
