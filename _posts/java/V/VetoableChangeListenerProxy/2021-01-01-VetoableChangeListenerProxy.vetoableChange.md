---
title: VetoableChangeListenerProxy.vetoableChange()
permalink: /Java/VetoableChangeListenerProxy/vetoableChange/
date: 2021-01-11
key: Java.V.VetoableChangeListenerProxy
category: Java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.4']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VetoableChangeListenerProxy.metodos valor="vetoableChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void vetoableChange(PropertyChangeEvent event) throws PropertyVetoException
~~~

## Parámetros
* **PropertyChangeEvent event**,  {% include w3api/param_description.html metodo=_dato parametro="PropertyChangeEvent event" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

## Clase Padre
[VetoableChangeListenerProxy](/Java/VetoableChangeListenerProxy/)

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
