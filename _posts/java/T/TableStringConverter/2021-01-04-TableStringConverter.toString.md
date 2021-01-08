---
title: TableStringConverter.toString()
permalink: Java/TableStringConverter/toString
date: 2021-01-04
key: JavaJava.T.TableStringConverter
category: java
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
* **int column**,  {% include w3api/param_description.html metodo=_data parametro="int column" %}
* **TableModel model**,  {% include w3api/param_description.html metodo=_data parametro="TableModel model" %}
* **int row**,  {% include w3api/param_description.html metodo=_data parametro="int row" %}

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
{%- for _ldc in site.data.Java.T.TableStringConverter.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
