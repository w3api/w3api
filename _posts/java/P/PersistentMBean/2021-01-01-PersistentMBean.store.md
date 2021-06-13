---
title: PersistentMBean.store()
permalink: /Java/PersistentMBean/store/
date: 2021-01-11
key: Java.P.PersistentMBean
category: java
tags: ['java se', 'javax.management', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.P.PersistentMBean.metodos valor="store" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void store() throws MBeanException, RuntimeOperationsException, InstanceNotFoundException
~~~

## Excepciones
[MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[PersistentMBean](/Java/PersistentMBean/)

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
