---
title: JMenuItem.JMenuItem()
permalink: Java/JMenuItem/JMenuItem
date: 2021-01-04
key: JavaJava.J.JMenuItem
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JMenuItem.constructores valor="JMenuItem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public JMenuItem()
public JMenuItem(String text)
public JMenuItem(String text, int mnemonic)
public JMenuItem(String text, Icon icon)
public JMenuItem(Action a)
public JMenuItem(Icon icon)
~~~

## Parámetros
* **String text**,  {% include w3api/param_description.html metodo=_data parametro="String text" %}
* **Icon icon**,  {% include w3api/param_description.html metodo=_data parametro="Icon icon" %}
* **Action a**,  {% include w3api/param_description.html metodo=_data parametro="Action a" %}
* **int mnemonic**,  {% include w3api/param_description.html metodo=_data parametro="int mnemonic" %}

## Clase Padre
[JMenuItem](/Java/JMenuItem/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JMenuItem.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
