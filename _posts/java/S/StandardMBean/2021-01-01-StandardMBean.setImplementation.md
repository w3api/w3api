---
title: StandardMBean.setImplementation()
permalink: /Java/StandardMBean/setImplementation/
date: 2021-01-11
key: Java.S.StandardMBean
category: Java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.S.StandardMBean.metodos valor="setImplementation" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setImplementation(Object implementation) throws NotCompliantMBeanException
~~~

## Parámetros
* **Object implementation**,  {% include w3api/param_description.html metodo=_dato parametro="Object implementation" %}

## Excepciones
[IllegalArgumentException](/Java/IllegalArgumentException/), [NotCompliantMBeanException](/Java/NotCompliantMBeanException/)

## Clase Padre
[StandardMBean](/Java/StandardMBean/)

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
