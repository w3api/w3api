---
title: FieldPosition.FieldPosition()
permalink: Java/FieldPosition/FieldPosition
date: 2021-01-04
key: JavaJava.F.FieldPosition
category: java
tags: ['java se', 'java.text', 'java.base', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.F.FieldPosition.constructores valor="FieldPosition" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public FieldPosition(int field)
public FieldPosition(Format.Field attribute)
public FieldPosition(Format.Field attribute, int fieldID)
~~~

## Parámetros
* **Format.Field attribute**,  {% include w3api/param_description.html metodo=_data parametro="Format.Field attribute" %}
* **int fieldID**,  {% include w3api/param_description.html metodo=_data parametro="int fieldID" %}
* **int field**,  {% include w3api/param_description.html metodo=_data parametro="int field" %}

## Clase Padre
[FieldPosition](/Java/FieldPosition/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.F.FieldPosition.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
