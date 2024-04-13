---
title: TableStringConverter.toString()
permalink: /Java/TableStringConverter/toString/
date: 2021-01-11
key: Java.T.TableStringConverter
category: Java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.6']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.T.TableStringConverter.metodos valor="toString" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public abstract String toString(TableModel model, int row, int column)
~~~

## Parámetros
* **TableModel model**,  {% include w3api/param_description.html metodo=_dato parametro="TableModel model" %}
* **int column**,  {% include w3api/param_description.html metodo=_dato parametro="int column" %}
* **int row**,  {% include w3api/param_description.html metodo=_dato parametro="int row" %}

## Excepciones
[IndexOutOfBoundsException](/Java/IndexOutOfBoundsException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[TableStringConverter](/Java/TableStringConverter/)

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
