---
title: DefaultListSelectionModel.setSelectionInterval()
permalink: Java/DefaultListSelectionModel/setSelectionInterval
date: 2021-01-04
key: JavaJava.D.DefaultListSelectionModel
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultListSelectionModel.metodos valor="setSelectionInterval" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setSelectionInterval(int index0, int index1)
~~~

## Parámetros
* **int index0**,  {% include w3api/param_description.html metodo=_data parametro="int index0" %}
* **int index1**,  {% include w3api/param_description.html metodo=_data parametro="int index1" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[DefaultListSelectionModel](/Java/DefaultListSelectionModel/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.D.DefaultListSelectionModel.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
