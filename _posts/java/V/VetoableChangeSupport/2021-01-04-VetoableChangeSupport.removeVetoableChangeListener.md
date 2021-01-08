---
title: VetoableChangeSupport.removeVetoableChangeListener()
permalink: Java/VetoableChangeSupport/removeVetoableChangeListener
date: 2021-01-04
key: JavaJava.V.VetoableChangeSupport
category: java
tags: ['java se', 'java.beans', 'java.desktop', 'metodo java', 'Java 1.1']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.V.VetoableChangeSupport.metodos valor="removeVetoableChangeListener" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void removeVetoableChangeListener(VetoableChangeListener listener)
public void removeVetoableChangeListener(String propertyName, VetoableChangeListener listener)
~~~

## Parámetros
* **VetoableChangeListener listener**,  {% include w3api/param_description.html metodo=_data parametro="VetoableChangeListener listener" %}
* **String propertyName**,  {% include w3api/param_description.html metodo=_data parametro="String propertyName" %}

## Clase Padre
[VetoableChangeSupport](/Java/VetoableChangeSupport/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.V.VetoableChangeSupport.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
