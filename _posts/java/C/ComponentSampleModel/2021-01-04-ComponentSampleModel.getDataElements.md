---
title: ComponentSampleModel.getDataElements()
permalink: Java/ComponentSampleModel/getDataElements
date: 2021-01-04
key: JavaJava.C.ComponentSampleModel
category: java
tags: ['java se', 'java.awt.image', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.C.ComponentSampleModel.metodos valor="getDataElements" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public Object getDataElements(int x, int y, Object obj, DataBuffer data)
~~~

## Parámetros
* **DataBuffer data**,  {% include w3api/param_description.html metodo=_data parametro="DataBuffer data" %}
* **int y**,  {% include w3api/param_description.html metodo=_data parametro="int y" %}
* **Object obj**,  {% include w3api/param_description.html metodo=_data parametro="Object obj" %}
* **int x**,  {% include w3api/param_description.html metodo=_data parametro="int x" %}

## Excepciones
[ArrayIndexOutOfBoundsException](/Java/ArrayIndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[ComponentSampleModel](/Java/ComponentSampleModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.C.ComponentSampleModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
