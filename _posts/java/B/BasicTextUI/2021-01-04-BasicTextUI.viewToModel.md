---
title: BasicTextUI.viewToModel()
permalink: Java/BasicTextUI/viewToModel
date: 2021-01-04
key: JavaJava.B.BasicTextUI
category: java
tags: ['java se', 'javax.swing.plaf.basic', 'java.desktop', 'metodo java', 'Java 1.0']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BasicTextUI.metodos valor="viewToModel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
@Deprecated(since="9") public int viewToModel(JTextComponent tc, Point pt)
@Deprecated(since="9") public int viewToModel(JTextComponent tc, Point pt, Position.Bias[] biasReturn)
~~~

## Parámetros
* **Position.Bias[] biasReturn**,  {% include w3api/param_description.html metodo=_data parametro="Position.Bias[] biasReturn" %}
* **Point pt**,  {% include w3api/param_description.html metodo=_data parametro="Point pt" %}
* **JTextComponent tc**,  {% include w3api/param_description.html metodo=_data parametro="JTextComponent tc" %}

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
