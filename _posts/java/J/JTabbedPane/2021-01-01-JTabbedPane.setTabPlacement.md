---
title: JTabbedPane.setTabPlacement()
permalink: Java/JTabbedPane/setTabPlacement
date: 2021-01-11
key: JavaJava.J.JTabbedPane
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTabbedPane.metodos valor="setTabPlacement" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, enumerationValues={"JTabbedPane.TOP","JTabbedPane.LEFT","JTabbedPane.BOTTOM","JTabbedPane.RIGHT"}, description="The tabbedpane\'s tab placement.") public void setTabPlacement(int tabPlacement)
~~~

## Parámetros
* **int tabPlacement**,  {% include w3api/param_description.html metodo=_dato parametro="int tabPlacement" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JTabbedPane](/Java/JTabbedPane/)

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
