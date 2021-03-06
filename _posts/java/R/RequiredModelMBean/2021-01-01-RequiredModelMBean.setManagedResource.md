---
title: RequiredModelMBean.setManagedResource()
permalink: /Java/RequiredModelMBean/setManagedResource/
date: 2021-01-11
key: Java.R.RequiredModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RequiredModelMBean.metodos valor="setManagedResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
public void setManagedResource(Object mr, String mr_type) throws MBeanException, RuntimeOperationsException, InstanceNotFoundException, InvalidTargetObjectTypeException
~~~

## Parámetros
* **Object mr**,  {% include w3api/param_description.html metodo=_dato parametro="Object mr" %}
* **String mr_type**,  {% include w3api/param_description.html metodo=_dato parametro="String mr_type" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [InvalidTargetObjectTypeException](/Java/InvalidTargetObjectTypeException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/)

## Clase Padre
[RequiredModelMBean](/Java/RequiredModelMBean/)

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
