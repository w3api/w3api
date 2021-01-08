---
title: UIManager.createLookAndFeel()
permalink: Java/UIManager/createLookAndFeel
date: 2021-01-04
key: JavaJava.U.UIManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIManager.metodos valor="createLookAndFeel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static LookAndFeel createLookAndFeel(String name) throws UnsupportedLookAndFeelException
~~~

## Parámetros
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}

## Excepciones
[UnsupportedLookAndFeelException](/Java/UnsupportedLookAndFeelException/), [NullPointerException](/Java/NullPointerException/)

## Clase Padre
[UIManager](/Java/UIManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.U.UIManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
