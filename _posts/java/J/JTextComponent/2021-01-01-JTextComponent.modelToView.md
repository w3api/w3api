---
title: JTextComponent.modelToView()
permalink: /Java/JTextComponent/modelToView/
date: 2021-01-11
key: Java.J.JTextComponent
category: Java
tags: ['java se', 'javax.swing.text', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JTextComponent.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public Rectangle modelToView(int pos) throws BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_dato parametro="int pos" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[JTextComponent](/Java/JTextComponent/)

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
