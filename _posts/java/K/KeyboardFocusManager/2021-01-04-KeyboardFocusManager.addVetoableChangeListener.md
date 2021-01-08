---
title: KeyboardFocusManager.addVetoableChangeListener()
permalink: Java/KeyboardFocusManager/addVetoableChangeListener
date: 2021-01-04
key: JavaJava.K.KeyboardFocusManager
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyboardFocusManager.metodos valor="addVetoableChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void addVetoableChangeListener(VetoableChangeListener listener)
public void addVetoableChangeListener(String propertyName, VetoableChangeListener listener)
~~~

## Parámetros
* **VetoableChangeListener listener**,  {% include w3api/param_description.html metodo=_data parametro="VetoableChangeListener listener" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}

## Clase Padre
[KeyboardFocusManager](/Java/KeyboardFocusManager/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.K.KeyboardFocusManager.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
