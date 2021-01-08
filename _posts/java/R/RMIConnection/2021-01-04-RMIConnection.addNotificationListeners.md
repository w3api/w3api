---
title: RMIConnection.addNotificationListeners()
permalink: Java/RMIConnection/addNotificationListeners
date: 2021-01-04
key: JavaJava.R.RMIConnection
category: java
tags: ['java se', 'javax.management.remote.rmi', 'java.management.rmi', 'metodo java', 'Java 1.5']
sidebar: 
  nav: java
---

{% include w3api/datos.html clase=site.data.Java.R.RMIConnection.metodos valor="addNotificationListeners" %}

## Descripción
{{_dato.description }}

## Sintaxis
~~~java
Integer[] addNotificationListeners(ObjectName[] names, MarshalledObject[] filters, Subject[] delegationSubjects) throws InstanceNotFoundException, IOException
~~~

## Parámetros
* **MarshalledObject[] filters**,  {% include w3api/param_description.html metodo=_data parametro="MarshalledObject[] filters" %}
* **ObjectName[] names**,  {% include w3api/param_description.html metodo=_data parametro="ObjectName[] names" %}
* **Subject[] delegationSubjects**,  {% include w3api/param_description.html metodo=_data parametro="Subject[] delegationSubjects" %}

## Excepciones
[SecurityException](/Java/SecurityException/), [InstanceNotFoundException](/Java/InstanceNotFoundException/), [IllegalArgumentException](/Java/IllegalArgumentException/), [ClassCastException](/Java/ClassCastException/), [IOException](/Java/IOException/)

## Clase Padre
[RMIConnection](/Java/RMIConnection/)

## Ejemplo
~~~java
{{ _dato.code}}
~~~

## Líneas de Código
<ul>
{%- for _ldc in site.data.Java.R.RMIConnection.ldc -%}
   <li>
       <a href="{{_ldc['url'] }}">{{ _ldc['nombre'] }}</a>
   </li>
{%- endfor -%}
</ul>
