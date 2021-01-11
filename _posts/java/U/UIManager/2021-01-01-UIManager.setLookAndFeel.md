---
title: UIManager.setLookAndFeel()
permalink: Java/UIManager/setLookAndFeel
date: 2021-01-11
key: JavaJava.U.UIManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIManager.metodos valor="setLookAndFeel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setLookAndFeel(String className) throws ClassNotFoundException, InstantiationException, IllegalAccessException, UnsupportedLookAndFeelException
public static void setLookAndFeel(LookAndFeel newLookAndFeel) throws UnsupportedLookAndFeelException
~~~

## Parámetros
* **LookAndFeel newLookAndFeel**,  {% include w3api/param_description.html metodo=_dato parametro="LookAndFeel newLookAndFeel" %}
* **String className**,  {% include w3api/param_description.html metodo=_dato parametro="String className" %}

## Excepciones
[ClassCastException](/Java/ClassCastException/), [UnsupportedLookAndFeelException](/Java/UnsupportedLookAndFeelException/), [ClassNotFoundException](/Java/ClassNotFoundException/), [IllegalAccessException](/Java/IllegalAccessException/), [InstantiationException](/Java/InstantiationException/)

## Clase Padre
[UIManager](/Java/UIManager/)

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
