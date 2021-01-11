---
title: DefaultRowSorter.ModelWrapper.getValueAt()
permalink: Java/DefaultRowSorter/ModelWrapper/getValueAt
date: 2021-01-11
key: JavaJava.D.DefaultRowSorter.ModelWrapper
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.D.DefaultRowSorter.ModelWrapper.metodos valor="getValueAt" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract Object getValueAt(int row, int column)
~~~

## Parámetros
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/)

## Clase Padre
[DefaultRowSorter.ModelWrapper](/Java/DefaultRowSorter/ModelWrapper/)

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