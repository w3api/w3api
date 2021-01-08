---
title: UIManager.setLookAndFeel()
permalink: Java/UIManager/setLookAndFeel
date: 2021-01-04
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
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **LookAndFeel newLookAndFeel**,  {% include w3api/param_description.html metodo=_data parametro="LookAndFeel newLookAndFeel" %}

## Excepciones
[InstantiationException](/Java/InstantiationException/), [IllegalAccessException](/Java/IllegalAccessException/), [UnsupportedLookAndFeelException](/Java/UnsupportedLookAndFeelException/), [ClassCastException](/Java/ClassCastException/), [ClassNotFoundException](/Java/ClassNotFoundException/)

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
