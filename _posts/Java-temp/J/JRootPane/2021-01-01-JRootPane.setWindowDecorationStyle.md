---
title: JRootPane.setWindowDecorationStyle()
permalink: /Java/JRootPane/setWindowDecorationStyle/
date: 2021-01-11
key: Java.J.JRootPane
category: Java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JRootPane.metodos valor="setWindowDecorationStyle" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@BeanProperty(expert=true, visualUpdate=true, enumerationValues={"JRootPane.NONE","JRootPane.FRAME","JRootPane.PLAIN_DIALOG","JRootPane.INFORMATION_DIALOG","JRootPane.ERROR_DIALOG","JRootPane.COLOR_CHOOSER_DIALOG","JRootPane.FILE_CHOOSER_DIALOG","JRootPane.QUESTION_DIALOG","JRootPane.WARNING_DIALOG"}, description="Identifies the type of Window decorations to provide") public void setWindowDecorationStyle(int windowDecorationStyle)
~~~

## Parámetros
* **int windowDecorationStyle**,  {% include w3api/param_description.html metodo=_dato parametro="int windowDecorationStyle" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[JRootPane](/Java/JRootPane/)

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
