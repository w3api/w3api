---
title: VetoableChangeListener.vetoableChange()
permalink: /Java/VetoableChangeListener/vetoableChange/
date: 2021-01-11
key: Java.V.VetoableChangeListener
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VetoableChangeListener.metodos valor="vetoableChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void vetoableChange(PropertyChangeEvent evt) throws PropertyVetoException
~~~

## Parámetros
* **PropertyChangeEvent evt**,  {% include w3api/param_description.html metodo=_dato parametro="PropertyChangeEvent evt" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

## Clase Padre
[VetoableChangeListener](/Java/VetoableChangeListener/)

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
