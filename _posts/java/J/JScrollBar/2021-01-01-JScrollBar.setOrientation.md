---
title: JScrollBar.setOrientation()
permalink: Java/JScrollBar/setOrientation
date: 2021-01-11
key: JavaJava.J.JScrollBar
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JScrollBar.metodos valor="setOrientation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(preferred=true, visualUpdate=true, enumerationValues={"JScrollBar.VERTICAL","JScrollBar.HORIZONTAL"}, description="The scrollbar\'s orientation.") public void setOrientation(int orientation)
~~~

## Parámetros
* **int orientation**,  {% include w3api/param_description.html metodo=_dato parametro="int orientation" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JScrollBar](/Java/JScrollBar/)

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
