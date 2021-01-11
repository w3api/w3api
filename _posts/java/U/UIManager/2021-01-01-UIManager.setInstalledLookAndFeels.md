---
title: UIManager.setInstalledLookAndFeels()
permalink: Java/UIManager/setInstalledLookAndFeels
date: 2021-01-11
key: JavaJava.U.UIManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIManager.metodos valor="setInstalledLookAndFeels" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setInstalledLookAndFeels(UIManager.LookAndFeelInfo[] infos) throws SecurityException
~~~

## Parámetros
* **UIManager.LookAndFeelInfo[] infos**,  {% include w3api/param_description.html metodo=_dato parametro="UIManager.LookAndFeelInfo[] infos" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [NullPointerException](/Java/NullPointerException/)

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
