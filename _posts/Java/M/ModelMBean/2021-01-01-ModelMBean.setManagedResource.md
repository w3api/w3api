---
title: ModelMBean.setManagedResource()
permalink: /Java/ModelMBean/setManagedResource/
date: 2021-01-11
key: Java.M.ModelMBean
category: Java
tags: ['java se', 'javax.management.modelmbean', 'java.management', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.M.ModelMBean.metodos valor="setManagedResource" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
void setManagedResource(Object mr, String mr_type) throws MBeanException, RuntimeOperationsException, InstanceNotFoundException, InvalidTargetObjectTypeException
~~~

## Parámetros
* **Object mr**,  {% include w3api/param_description.html metodo=_dato parametro="Object mr" %}
* **String mr_type**,  {% include w3api/param_description.html metodo=_dato parametro="String mr_type" %}

## Excepciones
[MBeanException](/Java/MBeanException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [RuntimeOperationsException](/Java/RuntimeOperationsException/), [InvalidTargetObjectTypeException](/Java/InvalidTargetObjectTypeException/)

## Clase Padre
[ModelMBean](/Java/ModelMBean/)

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
