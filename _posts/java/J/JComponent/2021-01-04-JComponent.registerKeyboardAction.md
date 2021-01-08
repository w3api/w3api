---
title: JComponent.registerKeyboardAction()
permalink: Java/JComponent/registerKeyboardAction
date: 2021-01-04
key: JavaJava.J.JComponent
category: java
tags: ['java se', 'javax.swing', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.J.JComponent.metodos valor="registerKeyboardAction" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void registerKeyboardAction(ActionListener anAction, String aCommand, KeyStroke aKeyStroke, int aCondition)
public void registerKeyboardAction(ActionListener anAction, KeyStroke aKeyStroke, int aCondition)
~~~

## Parámetros
* **String aCommand**,  {% include w3api/param_description.html metodo=_data parametro="String aCommand" %}
* **KeyStroke aKeyStroke**,  {% include w3api/param_description.html metodo=_data parametro="KeyStroke aKeyStroke" %}
* **int aCondition**,  {% include w3api/param_description.html metodo=_data parametro="int aCondition" %}
* **ActionListener anAction**,  {% include w3api/param_description.html metodo=_data parametro="ActionListener anAction" %}

## Clase Padre
[JComponent](/Java/JComponent/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.J.JComponent.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
