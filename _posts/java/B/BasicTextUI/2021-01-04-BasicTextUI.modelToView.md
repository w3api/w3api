---
title: BasicTextUI.modelToView()
permalink: Java/BasicTextUI/modelToView
date: 2021-01-04
key: JavaJava.B.BasicTextUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTextUI.metodos valor="modelToView" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public Rectangle modelToView(JTextComponent tc, int pos) throws BadLocationException
@Deprecated(since="9") public Rectangle modelToView(JTextComponent tc, int pos, Position.Bias bias) throws BadLocationException
~~~

## Parámetros
* **int pos**,  {% include w3api/param_description.html metodo=_data parametro="int pos" %}
* **Position.Bias bias**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias bias" %}
* **JTextComponent tc**,  {% include w3api/param_description.html metodo=_data parametro="JTextComponent tc" %}

## Excepciones
[BadLocationException](/Java/BadLocationException/)

## Clase Padre
[BasicTextUI](/Java/BasicTextUI/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BasicTextUI.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
