---
title: MultiTextUI.modelToView()
permalink: Java/MultiTextUI/modelToView
date: 2021-01-11
key: JavaJava.M.MultiTextUI
category: Java
tags: ['java se', 'javax.swing.plaf.multi', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.MultiTextUI.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public Rectangle modelToView(JTextComponent a, int b) throws BadLocationException
@Deprecated(since="9") public Rectangle modelToView(JTextComponent a, int b, Position.Bias c) throws BadLocationException
~~~

## Parámetros
* **int b**,  {% include w3api/param_description.html metodo=_dato parametro="int b" %}
* **JTextComponent a**,  {% include w3api/param_description.html metodo=_dato parametro="JTextComponent a" %}
* **Position.Bias c**,  {% include w3api/param_description.html metodo=_dato parametro="Position.Bias c" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[MultiTextUI](/Java/MultiTextUI/)

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
