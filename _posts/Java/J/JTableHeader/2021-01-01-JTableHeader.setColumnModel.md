---
title: JTableHeader.setColumnModel()
permalink: /Java/JTableHeader/setColumnModel/
date: 2021-01-11
key: Java.J.JTableHeader
category: Java
tags: ['java se', 'javax.swing.table', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTableHeader.metodos valor="setColumnModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(description="The object governing the way columns appear in the view.") public void setColumnModel(TableColumnModel columnModel)
~~~

## Parámetros
* **TableColumnModel columnModel**,  {% include w3api/param_description.html metodo=_dato parametro="TableColumnModel columnModel" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTableHeader](/Java/JTableHeader/)

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
