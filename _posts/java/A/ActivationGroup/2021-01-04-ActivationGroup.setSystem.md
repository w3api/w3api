---
title: ActivationGroup.setSystem()
permalink: Java/ActivationGroup/setSystem
date: 2021-01-04
key: JavaJava.A.ActivationGroup
category: java
tags: ['java se', 'java.rmi.activation', 'java.rmi', 'metodo java', 'Java 1.2']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.A.ActivationGroup.metodos valor="setSystem" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public static void setSystem(ActivationSystem system) throws ActivationException
~~~

## Parámetros
* **ActivationSystem system**,  {% include w3api/param_description.html metodo=_data parametro="ActivationSystem system" %}

## Excepciones
[ActivationException](/Java/ActivationException/), [SecurityException](/Java/SecurityException/), [UnsupportedOperationException](/Java/UnsupportedOperationException/)

## Clase Padre
[ActivationGroup](/Java/ActivationGroup/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.A.ActivationGroup.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
