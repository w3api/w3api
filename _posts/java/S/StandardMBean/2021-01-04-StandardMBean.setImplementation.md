---
title: StandardMBean.setImplementation()
permalink: Java/StandardMBean/setImplementation
date: 2021-01-04
key: JavaJava.S.StandardMBean
category: java
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
* **Object implementation**,  {% include w3api/param_description.html metodo=_data parametro="Object implementation" %}

## Excepciones
[NotCompliantMBeanException](/Java/NotCompliantMBeanException/), [IllegalArgumentException](/Java/IllegalArgumentException/)

## Clase Padre
[StandardMBean](/Java/StandardMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.S.StandardMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
