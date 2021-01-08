---
title: UIManager.installLookAndFeel()
permalink: Java/UIManager/installLookAndFeel
date: 2021-01-04
key: JavaJava.U.UIManager
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.U.UIManager.metodos valor="installLookAndFeel" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void installLookAndFeel(String name, String className)
public static void installLookAndFeel(UIManager.LookAndFeelInfo info)
~~~

## Parámetros
* **String className**,  {% include w3api/param_description.html metodo=_data parametro="String className" %}
* **String name**,  {% include w3api/param_description.html metodo=_data parametro="String name" %}
* **UIManager.LookAndFeelInfo info**,  {% include w3api/param_description.html metodo=_data parametro="UIManager.LookAndFeelInfo info" %}

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
