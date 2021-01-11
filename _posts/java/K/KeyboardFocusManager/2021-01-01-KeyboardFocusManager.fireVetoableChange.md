---
title: KeyboardFocusManager.fireVetoableChange()
permalink: Java/KeyboardFocusManager/fireVetoableChange
date: 2021-01-11
key: JavaJava.K.KeyboardFocusManager
category: java
tags: ['java se', 'java.awt', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.K.KeyboardFocusManager.metodos valor="fireVetoableChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
protected void fireVetoableChange(String propertyName, Object oldValue, Object newValue) throws PropertyVetoException
~~~

## Parámetros
* **String propertyName**,  {% include w3api/param_description.html metodo=_dato parametro="String propertyName" %}
* **Object oldValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object oldValue" %}
* **Object newValue**,  {% include w3api/param_description.html metodo=_dato parametro="Object newValue" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

## Clase Padre
[KeyboardFocusManager](/Java/KeyboardFocusManager/)

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
