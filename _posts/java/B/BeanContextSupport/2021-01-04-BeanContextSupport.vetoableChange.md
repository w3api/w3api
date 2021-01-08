---
title: BeanContextSupport.vetoableChange()
permalink: Java/BeanContextSupport/vetoableChange
date: 2021-01-04
key: JavaJava.B.BeanContextSupport
category: java
tags: ['java se', 'java.beans.beancontext', 'java.desktop', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.B.BeanContextSupport.metodos valor="vetoableChange" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void vetoableChange(PropertyChangeEvent pce) throws PropertyVetoException
~~~

## Parámetros
* **PropertyChangeEvent pce**,  {% include w3api/param_description.html metodo=_data parametro="PropertyChangeEvent pce" %}

## Excepciones
[PropertyVetoException](/Java/PropertyVetoException/)

## Clase Padre
[BeanContextSupport](/Java/BeanContextSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.B.BeanContextSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
