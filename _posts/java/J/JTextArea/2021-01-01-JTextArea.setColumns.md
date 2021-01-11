---
title: JTextArea.setColumns()
permalink: Java/JTextArea/setColumns
date: 2021-01-11
key: JavaJava.J.JTextArea
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextArea.metodos valor="setColumns" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(bound=false, description="the number of columns preferred for display") public void setColumns(int columns)
~~~

## Parámetros
* **int columns**,  {% include w3api/param_description.html metodo=_dato parametro="int columns" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTextArea](/Java/JTextArea/)

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
