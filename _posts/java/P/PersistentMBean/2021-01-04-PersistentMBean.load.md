---
title: PersistentMBean.load()
permalink: Java/PersistentMBean/load
date: 2021-01-04
key: JavaJava.P.PersistentMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistentMBean.metodos valor="load" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void load() throws MBeanException, RuntimeOperationsException, InstanceNotFoundException
~~~

## Excepciones
[InstanceNotFoundException](/Java/InstanceNotFoundException/), [MBeanException](/Java/MBeanException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[PersistentMBean](/Java/PersistentMBean/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.P.PersistentMBean.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
